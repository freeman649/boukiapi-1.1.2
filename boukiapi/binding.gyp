{
  "targets": [
    {
      "target_name": "boukiapi",
      "sources": [ "src/boukiapi.cpp" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "include"
      ],
      "libraries": [
        "-lcrypt32.lib"
      ]
    }
  ]
}