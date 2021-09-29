# ガター内の緑色のボタンを押すとスクリプトを実行します。

def printf(text):
    assembly = "\t.section	__TEXT,__text,regular,pure_instructions\n"
    assembly += "\t.build_version macos, 11, 0	sdk_version 11, 3\n"
    assembly += "\t.globl	_main                           ; -- Begin function main\n"
    assembly += "\t.p2align	2\n"
    assembly += "_main:                                  ; @main\n"
    assembly += "\t.cfi_startproc\n"
    assembly += "; %bb.0:\n"
    assembly += "\tsub	sp, sp, #32                     ; =32\n"
    assembly += "\tstp	x29, x30, [sp, #16]             ; 16-byte Folded Spill\n"
    assembly += "\tadd	x29, sp, #16                    ; =16\n"
    assembly += "\t.cfi_def_cfa w29, 16\n"
    assembly += "\t.cfi_offset w30, -8\n"
    assembly += "\t.cfi_offset w29, -16\n"
    assembly += "\tmov	w8, #0\n"
    assembly += "\tstr	w8, [sp, #8]                    ; 4-byte Folded Spill\n"
    assembly += "\tstur	wzr, [x29, #-4]\n"
    assembly += "\tadrp	x0, l_.str@PAGE\n"
    assembly += "\tadd	x0, x0, l_.str@PAGEOFF\n"
    assembly += "\tbl	_printf\n"
    assembly += "\tldr	w0, [sp, #8]                    ; 4-byte Folded Reload\n"
    assembly += "\tldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload\n"
    assembly += "\tadd	sp, sp, #32                     ; =32\n"
    assembly += "\tret\n"
    assembly += "\t.cfi_endproc\n"
    assembly += "\t                                    ; -- End function\n"
    assembly += "\t.section	__TEXT,__cstring,cstring_literals\n"
    assembly += "l_.str:                                 ; @.str\n"
    assembly += f"\t.asciz	\"{text}\"\n"
    assembly += ".subsections_via_symbols"
    return assembly


def exportToFile(path, text):
    with open(path, "w") as f:
        f.write(text)


if __name__ == '__main__':
    assembly = printf("hello, world!!\n")
    exportToFile("./assm/main.s", assembly)
