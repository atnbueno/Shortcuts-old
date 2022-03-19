# SFSymbols PNG experiment

I rescued an old idea to change the colors of a PNG by replacing a substring when they're Base64-encoded,
and applied it to a set of SFSymbols 1.1 I found somewhere [[?]](https://github.com/ActuallyZach/Shortcuts/tree/master/SFSymbols).

The images are at a resolution of 123&times;123 pixels, and they can be circumscribed without cropping, so they can be used as icons in a
[shortcut menu](https://www.reddit.com/r/shortcuts/comments/g4mrj4/guide_on_creating_menus_with_icons_vcard_menus/).
Unfortunately since iOS 14 transparent backgrounds can't be used for this (the background becomes white).

## How to use

Load `SFSymbols.json` and concatenate the "prefix" string, the desired color from "palette" (e.g. "palette.red"),
and the desired icon from "symbols" (e.g. "symbols.qrcode_viewfinder"). The symbol keys are named the same as the corresponding SFSymbol
but replacing periods (".") by underscores ("\_"). Decode the concatenated string to get the recolored PNG.

## More colors?

Use the `color2plte.py` script to get the substring for other monochrome 8-color palettes.
