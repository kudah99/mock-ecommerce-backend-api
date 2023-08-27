from fastapi_offline import FastAPIOffline
from starlette.middleware.cors import CORSMiddleware
from app.core.config import configs
from app.util.class_object import singleton


@singleton
class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPIOffline(
                title=configs.PROJECT_NAME,
                description="",
                version="0.0.1",
                contact={
                    "name": "Kuda",
                    "email": "kcchipangura@gmail.com",
                    },
               openapi_url=f"{configs.API}/openapi.json"
               )


        # set cors
        if configs.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

app_creator = AppCreator()
app = app_creator.app