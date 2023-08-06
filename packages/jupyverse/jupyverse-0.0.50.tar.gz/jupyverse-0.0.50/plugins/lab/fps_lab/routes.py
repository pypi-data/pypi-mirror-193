import json
import sys
from http import HTTPStatus
from pathlib import Path

import json5  # type: ignore
import pkg_resources  # type: ignore
from babel import Locale  # type: ignore
from fastapi import Depends, Response, status
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fps_auth_base import User, current_user, update_user  # type: ignore
from fps_frontend.config import get_frontend_config  # type: ignore
from starlette.requests import Request  # type: ignore

import jupyverse  # type: ignore

from .utils import get_federated_extensions

try:
    import jupyterlab  # type: ignore
    from fps_jupyterlab.config import get_jlab_config  # type: ignore

    jlab_dev_mode = get_jlab_config().dev_mode
except Exception:
    jlab_dev_mode = False


LOCALE = "en"


prefix_dir = Path(sys.prefix)
if jlab_dev_mode:
    jlab_dir = Path(jupyterlab.__file__).parents[1] / "dev_mode"
else:
    jlab_dir = prefix_dir / "share" / "jupyter" / "lab"


def init_router(router, redirect_after_root):
    extensions_dir = prefix_dir / "share" / "jupyter" / "labextensions"
    federated_extensions, disabled_extensions = get_federated_extensions(extensions_dir)

    for ext in federated_extensions:
        name = ext["name"]
        router.mount(
            f"/lab/extensions/{name}/static",
            StaticFiles(directory=extensions_dir / name / "static"),
            name=name,
        )

    router.mount(
        "/lab/api/themes",
        StaticFiles(directory=jlab_dir / "themes"),
        name="themes",
    )

    @router.get("/", name="root")
    async def get_root(
        response: Response,
        frontend_config=Depends(get_frontend_config),
        user: User = Depends(current_user()),
    ):
        # auto redirect
        response.status_code = status.HTTP_302_FOUND
        response.headers["Location"] = frontend_config.base_url + redirect_after_root

    @router.get("/favicon.ico")
    async def get_favicon():
        return FileResponse(Path(jupyverse.__file__).parent / "static" / "favicon.ico")

    @router.get("/static/notebook/components/MathJax/{rest_of_path:path}")
    async def get_mathjax(rest_of_path):
        return RedirectResponse(
            "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/" + rest_of_path
        )

    @router.get("/lab/api/listings/@jupyterlab/extensionmanager-extension/listings.json")
    async def get_listings(user: User = Depends(current_user())):
        return {
            "blocked_extensions_uris": [],
            "allowed_extensions_uris": [],
            "blocked_extensions": [],
            "allowed_extensions": [],
        }

    @router.get("/lab/api/extensions")
    async def get_extensions(user: User = Depends(current_user())):
        return federated_extensions

    @router.get("/lab/api/translations/")
    async def get_translations_(
        frontend_config=Depends(get_frontend_config),
        user: User = Depends(current_user()),
    ):
        return RedirectResponse(f"{frontend_config.base_url}lab/api/translations")

    @router.get("/lab/api/translations")
    async def get_translations(user: User = Depends(current_user())):
        locale = Locale.parse("en")
        data = {
            "en": {
                "displayName": locale.get_display_name(LOCALE).capitalize(),
                "nativeName": locale.get_display_name().capitalize(),
            }
        }
        for ep in pkg_resources.iter_entry_points(group="jupyterlab.languagepack"):
            locale = Locale.parse(ep.name)
            data[ep.name] = {
                "displayName": locale.get_display_name(LOCALE).capitalize(),
                "nativeName": locale.get_display_name().capitalize(),
            }
        return {"data": data, "message": ""}

    @router.get("/lab/api/translations/{language}")
    async def get_translation(
        language,
        user: User = Depends(current_user()),
    ):
        global LOCALE
        if language == "en":
            LOCALE = language
            return {}
        for ep in pkg_resources.iter_entry_points(group="jupyterlab.languagepack"):
            if ep.name == language:
                break
        else:
            return {"data": {}, "message": f"Language pack '{language}' not installed!"}
        LOCALE = language
        package = ep.load()
        data = {}
        for path in (Path(package.__file__).parent / "locale" / language / "LC_MESSAGES").glob(
            "*.json"
        ):
            with open(path) as f:
                data.update({path.stem: json.load(f)})
        return {"data": data, "message": ""}

    @router.get("/lab/api/settings/{name0}/{name1}:{name2}")
    async def get_setting(
        name0,
        name1,
        name2,
        user: User = Depends(current_user()),
    ):
        with open(jlab_dir / "static" / "package.json") as f:
            package = json.load(f)
        if name0 in ["@jupyterlab", "@retrolab"]:
            schemas_parent = jlab_dir
        else:
            schemas_parent = extensions_dir / name0 / name1
        with open(schemas_parent / "schemas" / name0 / name1 / f"{name2}.json") as f:
            schema = json.load(f)
        key = f"{name1}:{name2}"
        setting = {
            "id": f"@jupyterlab/{key}",
            "schema": schema,
            "version": package["version"],
            "raw": "{}",
            "settings": {},
            "last_modified": None,
            "created": None,
        }
        if user:
            user_settings = json.loads(user.settings)
            if key in user_settings:
                setting.update(user_settings[key])
                setting["settings"] = json5.loads(user_settings[key]["raw"])
        return setting

    @router.put(
        "/lab/api/settings/@jupyterlab/{name0}:{name1}",
        status_code=204,
    )
    async def change_setting(
        request: Request,
        name0,
        name1,
        user: User = Depends(current_user()),
        user_update=Depends(update_user),
    ):
        settings = json.loads(user.settings)
        settings[f"{name0}:{name1}"] = await request.json()
        await user_update({"settings": json.dumps(settings)})
        return Response(status_code=HTTPStatus.NO_CONTENT.value)

    @router.get("/lab/api/settings")
    async def get_settings(user: User = Depends(current_user())):
        with open(jlab_dir / "static" / "package.json") as f:
            package = json.load(f)
        if user:
            user_settings = json.loads(user.settings)
        else:
            user_settings = {}
        settings = []
        for path in (jlab_dir / "schemas" / "@jupyterlab").glob("*/*.json"):
            with open(path) as f:
                schema = json.load(f)
            key = f"{path.parent.name}:{path.stem}"
            setting = {
                "id": f"@jupyterlab/{key}",
                "schema": schema,
                "version": package["version"],
                "raw": "{}",
                "settings": {},
                "warning": None,
                "last_modified": None,
                "created": None,
            }
            if key in user_settings:
                setting.update(user_settings[key])
                setting["settings"] = json5.loads(user_settings[key]["raw"])
            settings.append(setting)
        return {"settings": settings}

    return prefix_dir, federated_extensions
