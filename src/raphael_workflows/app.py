"""Raphael service: raphael-workflows."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from raphael_contracts.errors import ErrorResponse
from raphael_workflows.routes import router

app = FastAPI(
    title="raphael-workflows",
    description="Approval/review/publish workflow engine",
    version="0.1.0",
    openapi_url="/v1/workflows/openapi.json" if "/v1/workflows" else "/openapi.json",
)

app.include_router(router, prefix="/v1/workflows" if "/v1/workflows" else "")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "raphael-workflows"}


@app.exception_handler(Exception)
async def unhandled(_request, exc: Exception) -> JSONResponse:
    err = ErrorResponse(code="internal_error", message=str(exc))
    return JSONResponse(status_code=500, content=err.model_dump())
