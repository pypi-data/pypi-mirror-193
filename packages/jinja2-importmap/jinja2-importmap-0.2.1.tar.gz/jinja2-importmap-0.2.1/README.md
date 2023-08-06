# `jinja2-importmap`

This package provides a simple tool for generating import maps from a directory
in the usual `node_modules` format. 

This can be done either from a directory, or from the contents of a Python package, 
for example if lists vendored JS dependencies in MANIFEST.in. 

## Use from Command Line

This package also provides a matching command line tool, `jinja2_importmap`:

```bash
$ jinja2_importmap demo/node_modules --prefix="url/prefix"                                                                                                                                                  19.7.0  jinja2-importmap
{
    "imports": {
        "codemirror": "url/prefix/codemirror/dist/index.js",
        "crelt": "url/prefix/crelt/index.es.js",
        ".yarn-integrity": "url/prefix/None",
        "w3c-keyname": "url/prefix/w3c-keyname/index.es.js",
        "@codemirror/lint": "url/prefix/@codemirror/lint/dist/index.js",
        "@codemirror/autocomplete": "url/prefix/@codemirror/autocomplete/dist/index.js",
        "@codemirror/language": "url/prefix/@codemirror/language/dist/index.js",
        "@codemirror/state": "url/prefix/@codemirror/state/dist/index.js",
        "@codemirror/search": "url/prefix/@codemirror/search/dist/index.js",
        "@codemirror/view": "url/prefix/@codemirror/view/dist/index.js",
        "@codemirror/commands": "url/prefix/@codemirror/commands/dist/index.js",
        "style-mod": "url/prefix/style-mod/src/style-mod.js",
        "@lezer/highlight": "url/prefix/@lezer/highlight/dist/index.js",
        "@lezer/common": "url/prefix/@lezer/common/dist/index.js",
        "@lezer/lr": "url/prefix/@lezer/lr/dist/index.js"
    }
}%
```

You can also equivalently use `python -m jinja2_importmap` to run the tool, or import 
`jinja2_importmap.core.scan_packages` for use in your own code.

## Use from Jinja Template

Currently, a custom parsed tag is not yet implemented. However, loading 
the `jinja2_importmap.ext.importmap`extension will currently add `importmap`
(an alias to `scan_packages`) to the global namespace.

```jinja
{{ importmap("web/static/vendor", package="my_package", prefix="static") }}
```

The intention is to eventually provide:

```jinja
{% importmap "web/static/vendor" package="my_package" prefix="static" %}
```

...or to allow overrides within a block:

```jinja
{% importmap "web/static/vendor" package="my_package" prefix="static" %}
    {# override automatically generated importmap with json provided here #}
{% endimportmap %}
```
