# raphael-workflows

Approval/review/publish workflow engine

## API

- Prefix: `/v1/workflows`
- Port: `8094`
- Health: `GET /health`

## Events

_Published and consumed events documented in `openapi.yaml` and raphael-contracts._

## Development

```bash
uv sync
uv run uvicorn raphael_workflows.app:app --reload --port 8094
```

Part of the [Raphael Platform](https://github.com/hummingbird-labs) by HummingBird Labs.
