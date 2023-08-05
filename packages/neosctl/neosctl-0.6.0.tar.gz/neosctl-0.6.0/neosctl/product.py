import json
import os
import pathlib
import typing

import httpx
import typer

from neosctl import constant, schema, util
from neosctl.auth import ensure_login
from neosctl.util import process_response

app = typer.Typer()


def _product_url(ctx: typer.Context) -> str:
    return "{}/product".format(ctx.obj.get_gateway_api_url().rstrip("/"))


special_delimiters = {
    r"\t": "\t",
}


@app.command(name="template")
def template(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
    filepath: str = typer.Option(..., "--filepath", "-f", help="Filepath of the csv template", callback=util.sanitize),
    output_dir: str = typer.Option(
        ...,
        "--output-dir",
        "-o",
        help="Output directory for the json template",
        callback=util.sanitize,
    ),
    delimiter: str = typer.Option(",", "--delimiter", "-d", help="csv delimiter", callback=util.sanitize),
    quotechar: typing.Optional[str] = typer.Option(
        None,
        "--quote-char",
        "-q",
        help="csv quote char",
        callback=util.sanitize,
    ),
) -> None:
    """Generate a data product schema template from a csv.

    Given a csv with a header row, generate a template field schema.
    """

    @ensure_login
    def _request(ctx: typer.Context, f: typing.IO) -> httpx.Response:
        params = {k: v for k, v in [("delimiter", delimiter), ("quotechar", quotechar)] if v is not None}

        return util.post(
            ctx,
            f"{_product_url(ctx)}/template",
            params=params,
            files={"csv_file": f},
        )

    fp = util.get_file_location(filepath)

    with fp.open("rb") as f:
        r = _request(ctx, f)

    if r.status_code >= constant.BAD_REQUEST_CODE:
        process_response(r)

    fp = pathlib.Path(output_dir) / f"{name}.json"
    with fp.open("w") as f:
        json.dump(r.json(), f, indent=4)


@app.command(name="create-stored")
def create_stored(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
    description: typing.Optional[str] = typer.Option(
        None,
        "--description",
        "-d",
        help="Data Product description",
        callback=util.sanitize,
    ),
    filepath: typing.Optional[str] = typer.Option(
        None,
        "--filepath",
        "-f",
        help="Filepath of the table schema json payload",
        callback=util.sanitize,
    ),
) -> None:
    """Create a stored data product."""

    @ensure_login
    def _request(ctx: typer.Context, dpc: schema.CreateStoredDataProduct) -> httpx.Response:
        return util.post(
            ctx,
            f"{_product_url(ctx)}/{name}",
            json=dpc.dict(exclude_none=True, by_alias=True),
        )

    fields = None
    if filepath:
        fp = util.get_file_location(filepath)
        fields = util.load_fields_file(fp)

    dpc = schema.CreateStoredDataProduct(
        name=name,
        description=description or "",
        details=schema.StoredSchemaBase(
            type="stored",
            fields=fields,
        ),
    )

    r = _request(ctx, dpc)
    process_response(r)


@app.command(name="create-streaming")
def create_streaming(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
    description: typing.Optional[str] = typer.Option(
        None,
        "--description",
        "-d",
        help="Data Product description",
        callback=util.sanitize,
    ),
    flow_type: str = typer.Option(..., "--flow-type", "-t", help="Flow type", callback=util.sanitize),
    filepath: typing.Optional[str] = typer.Option(
        None,
        "--filepath",
        "-f",
        help="Filepath of the table schema json payload",
        callback=util.sanitize,
    ),
) -> None:
    """Create a streaming data product."""

    @ensure_login
    def _request(ctx: typer.Context, dpc: schema.CreateStreamingDataProduct) -> httpx.Response:
        return util.post(
            ctx,
            f"{_product_url(ctx)}/{name}",
            json=dpc.dict(exclude_none=True, by_alias=True),
        )

    fields = None
    if filepath:
        fp = util.get_file_location(filepath)
        fields = util.load_fields_file(fp)

    dpc = schema.CreateStreamingDataProduct(
        name=name,
        description=description or "",
        details=schema.CreateStreamingSchema(
            type="streaming",
            fields=fields,
            flow_type=flow_type,
        ),
    )
    # TODO: support iceberg properties and orc bloom

    r = _request(ctx, dpc)
    process_response(r)


@app.command(name="add-schema-stored")
def add_schema_stored(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
    filepath: str = typer.Option(
        ...,
        "--filepath",
        "-f",
        help="Filepath of the table schema json payload",
        callback=util.sanitize,
    ),
) -> None:
    """Add a schema to a stored data product."""

    @ensure_login
    def _request(ctx: typer.Context, dps: schema.UpdateStoredSchema) -> httpx.Response:
        return util.post(
            ctx,
            f"{_product_url(ctx)}/{name}/schema",
            json=dps.dict(exclude_none=True, by_alias=True),
        )

    fp = util.get_file_location(filepath)
    fields = util.load_fields_file(fp)

    dps = schema.UpdateStoredSchema(details=schema.StoredDataProductSchema(type="stored", fields=fields))

    r = _request(ctx, dps)
    process_response(r)


@app.command(name="add-schema-streaming")
def add_schema_streaming(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
    filepath: str = typer.Option(
        ...,
        "--filepath",
        "-f",
        help="Filepath of the table schema json payload",
        callback=util.sanitize,
    ),
) -> None:
    """Add a schema to a streaming data product."""

    @ensure_login
    def _request(ctx: typer.Context, dps: schema.UpdateStreamingSchema) -> httpx.Response:
        return util.post(
            ctx,
            f"{_product_url(ctx)}/{name}",
            json=dps.dict(exclude_none=True, by_alias=True),
        )

    fp = util.get_file_location(filepath)
    fields = util.load_fields_file(fp)

    dps = schema.UpdateStreamingSchema(details=schema.StreamingDataProductSchema(type="streaming", fields=fields))
    # TODO: support iceberg properties and orc bloom

    r = _request(ctx, dps)
    process_response(r)


@app.command(name="create-subset")
def create_subset(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
    description: typing.Optional[str] = typer.Option(
        None,
        "--description",
        "-d",
        help="Data Product description",
        callback=util.sanitize,
    ),
    parent: str = typer.Option(..., "--parent", "-p", help="Data product parent", callback=util.sanitize),
    columns: typing.List[str] = typer.Option(
        ...,
        "--column",
        "-c",
        help="Parent column(s) to include",
        callback=util.sanitize,
    ),
) -> None:
    """Create a subset data product."""

    @ensure_login
    def _request(ctx: typer.Context, dpc: schema.CreateSubsetDataProduct) -> httpx.Response:
        return util.post(
            ctx,
            f"{_product_url(ctx)}/{name}",
            json=dpc.dict(exclude_none=True, by_alias=True),
        )

    dpc = schema.CreateSubsetDataProduct(
        name=name,
        description=description or "",
        details=schema.SubsetSchema(
            type="subset",
            parent_product=parent,
            columns=columns,
        ),
    )

    r = _request(ctx, dpc)
    process_response(r)


@app.command(name="list")
def list_products(ctx: typer.Context) -> None:
    """List data products."""

    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(ctx, _product_url(ctx))

    r = _request(ctx)
    process_response(r)


@app.command()
def delete_data(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
) -> None:
    """Delete data from a data product."""

    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            f"{_product_url(ctx)}/{name}/data",
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def delete(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
    *,
    force: bool = typer.Option(
        False,
        "--force",
        help="Force remove even if attached spark application is still running.",
    ),
) -> None:
    """Delete a data product."""

    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            f"{_product_url(ctx)}/{name}",
            params={"force": force},
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def publish(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
) -> None:
    """Publish a data product."""

    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.post(
            ctx,
            f"{_product_url(ctx)}/{name}/publish",
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def unpublish(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name", callback=util.sanitize),
) -> None:
    """Unpublish a product."""

    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            f"{_product_url(ctx)}/{name}/publish",
        )

    r = _request(ctx)
    process_response(r)


@app.command(name="get")
def get_product(
    ctx: typer.Context,
    product_name: str = typer.Argument(
        os.getenv("NEOSCTL_PRODUCT", ...),
        help="Data Product name",
        callback=util.sanitize,
    ),
) -> None:
    """Get data product schema."""

    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(
            ctx,
            f"{_product_url(ctx)}/{product_name}",
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def preview(
    ctx: typer.Context,
    product_name: str = typer.Argument(
        os.getenv("NEOSCTL_PRODUCT", ...),
        help="Data Product name",
        callback=util.sanitize,
    ),
) -> None:
    """Preview data product data.

    Get the first 25 rows of a data product's data.
    """

    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(
            ctx,
            "{product_url}/{name}/data".format(
                product_url=_product_url(ctx),
                name=product_name,
            ),
        )

    r = _request(ctx)
    process_response(r)
