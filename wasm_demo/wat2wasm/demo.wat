(module
    (func $add (param $x i32)(param $y i32)(result i32)
        local.get $x
        local.get $y
        i32.add 
    )
    (func $square (param $x i32)(result i32)
        local.get $x
        local.get $x
        i32.mul 
    )
    (export "add" (func $add))
    (export "square" (func $square))
)
