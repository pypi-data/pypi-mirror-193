```
 ______     ______   ______     ______     __
/\  ___\   /\__  _\ /\  ___\   /\  __ \   /\ \
\ \___  \  \/_/\ \/ \ \  __\   \ \  __ \  \ \ \____
 \/\_____\    \ \_\  \ \_____\  \ \_\ \_\  \ \_____\
  \/_____/     \/_/   \/_____/   \/_/\/_/   \/_____/

                 (teal makes sense)
```

## Write meaningful teal in s-expressions!

Steal aims to simplify the process of writing Algorand TEAL programs using s-expressions. With this cross-compiler, you can easily write TEAL programs that are compatible with the Algorand AVM. This tool is designed to make programming in TEAL more accessible, even for those with little or no experience. Whether you're a beginner or an experienced developer, this tool is perfect for anyone looking to write Algorand smart contracts in a more efficient and streamlined way. So, if you're looking to develop on the Algorand blockchain, this tool is definitely worth checking out.

## Examples

### Box

```
#pragma.version.8

(box_put "BoxA" "this is a test of a very very very very long string")

(assert (== 51 (box_len "BoxA")))
```

Output:

```
#pragma version 8
byte "BoxA"
byte "this is a test of a very very very very long string"
box_put
int 51
byte "BoxA"
box_len
==
assert
```

### Loops

```
#pragma.version.4

0
(loop:
  (bnz.loop
    (<= (dup (+ 1)) 10))
)
```

Output:

```
#pragma version 4
int 0
loop:
int 1
+
dup
int 10
<=
bnz loop
```

### Subroutines

```
#pragma.version.8

b.main

(my_subroutine: (retsub +))

(main: (return (callsub.my_subroutine 1 5)))
```

Output:

```
#pragma version 8
b main
my_subroutine:
+
retsub
main:
int 1
int 5
callsub my_subroutine
return
```

# Inner Transactions

```
#pragma.version.8

(itxn_submit
    itxn_begin
    (itxn_field.AssetAmount 1000)
    (itxn_field.XferAsset txn.Assets.0)
    (itxn_field.AssetReceiver txn.Sender)
    (itxn_field.TypeEnum int.axfer)
)
```

Output:

```
#pragma version 8
itxn_begin
int 1000
itxn_field AssetAmount
txn Assets 0
itxn_field XferAsset
txn Sender
itxn_field AssetReceiver
int axfer
itxn_field TypeEnum
itxn_submit

```

### Sample Program 1

```
#pragma.version.8

(&&
  (&&
    (== txn.RekeyTo global.ZeroAddress)
    (< txn.Fee 1000000)
  )
  (||
    (&&
      (> 67240 txn.FirstValid)
      (&&
        (== txn.Receiver addr.RFGEHKTFSLPIEGZYNVYALM6J4LJX4RPWERDWYS2PFKNVDWW3NG7MECQTJY)
        (== txn.CloseRemainderTo addr.RFGEHKTFSLPIEGZYNVYALM6J4LJX4RPWERDWYS2PFKNVDWW3NG7MECQTJY)
      )
    )
    (&&
      (== byte.base64.QzYhq9JlYbn2QdOMrhyxVlNtNjeyvyJc/I8d8VAGfGc= (sha256 arg.0))
      (&&
        (== 46 (len arg.0))
        (&&
          (== txn.Receiver addr.SOEI4UA72A7ZL5P25GNISSVWW724YABSGZ7GHW5ERV4QKK2XSXLXGXPG5Y)
          (== txn.CloseRemainderTo addr.SOEI4UA72A7ZL5P25GNISSVWW724YABSGZ7GHW5ERV4QKK2XSXLXGXPG5Y)
        )
      )
    )
  )
)
```

Output:

```
#pragma version 8
txn RekeyTo
global ZeroAddress
==
txn Fee
int 1000000
<
&&
int 67240
txn FirstValid
>
txn Receiver
addr RFGEHKTFSLPIEGZYNVYALM6J4LJX4RPWERDWYS2PFKNVDWW3NG7MECQTJY
==
txn CloseRemainderTo
addr RFGEHKTFSLPIEGZYNVYALM6J4LJX4RPWERDWYS2PFKNVDWW3NG7MECQTJY
==
&&
&&
byte base64 QzYhq9JlYbn2QdOMrhyxVlNtNjeyvyJc/I8d8VAGfGc=
arg 0
sha256
==
int 46
arg 0
len
==
txn Receiver
addr SOEI4UA72A7ZL5P25GNISSVWW724YABSGZ7GHW5ERV4QKK2XSXLXGXPG5Y
==
txn CloseRemainderTo
addr SOEI4UA72A7ZL5P25GNISSVWW724YABSGZ7GHW5ERV4QKK2XSXLXGXPG5Y
==
&&
&&
&&
||
&&
```

## How To Compile

Compilation cli is quite primitive at the moment.

```bash
% python -m steal examples/prog1.steal > examples/build/prog1.teal
```

## Disclaimer

Very much in early stages, please use it at your own risk.

## Licence

Copyright (c) 2023 Kadir Pekel.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
