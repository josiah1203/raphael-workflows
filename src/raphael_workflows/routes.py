"""API routes for raphael-workflows."""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(tags=["raphael-workflows"])


@router.get("")
def list_root() -> dict[str, str]:
  return {"service": "raphael-workflows", "status": "stub"}
