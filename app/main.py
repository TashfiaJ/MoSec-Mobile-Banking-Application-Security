from fastapi import FastAPI
from contextlib import asynccontextmanager
import os
from app.controllers.apk_controller import apk_router
from app.controllers.analysis_controller import analysis_router
from app.controllers.ssl_tls_controller import ssl_tls_router
from app.controllers.manual_analysis_controller import manual_analysis_router
from app.controllers.reverse_engineering_controller import reverse_engineering_router
from app.controllers.sensitive_data_controller import sensitive_data_router
from app.controllers.cwe_controller import cwe_router
from fastapi.middleware.cors import CORSMiddleware

# Set Java path
JAVA_HOME = r"C:/Program Files/Java/jdk-23"
os.environ["JAVA_HOME"] = JAVA_HOME
os.environ["PATH"] += os.pathsep + os.path.join(JAVA_HOME, "bin")

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Validating environment...")
        if os.system("java -version") != 0:
            raise RuntimeError("Java is not properly configured.")
        if os.system(r'C:/Users/HP/Documents/apktool/apktool.bat --version') != 0:
            raise RuntimeError("Apktool is not properly configured.")
        print("Environment validated.")
    except Exception as e:
        raise RuntimeError(f"Environment setup failed: {e}")

    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(apk_router, prefix="/apk")
app.include_router(analysis_router, prefix="/analysis")
app.include_router(ssl_tls_router, prefix="/ssl-tls")
app.include_router(manual_analysis_router, prefix="/api/v1", tags=["Manual Analysis"])
app.include_router(reverse_engineering_router, prefix="/api/v1", tags=["Reverse Engineering"])
app.include_router(sensitive_data_router, prefix="/api/v1", tags=["Sensitive Data Leakage Detection"])
app.include_router(cwe_router, prefix="/api/v1", tags=["CWE Analysis"])
