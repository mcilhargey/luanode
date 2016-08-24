{
    "targets": [{
        "target_name": "luanode",
        "product_extension": "node",
        "type": "shared_library",
        "include_dirs": [
            "include"
        ],
        "libraries": [
            "../lib/liblua53.a",
        ],
        "sources": [
            "src/values.cc",
            "src/luastate.cc",
            "src/luanode.cc"
        ]
    }]
}
