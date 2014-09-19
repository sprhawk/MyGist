GDB
===

0. start ( GDB server )

    target remote localhost:2331    
    mon flash breakpoints = 1       
    monitor reset                   
    file $(OUTPUT_BINARY_DIRECTORY)/$(OUTPUT_FILENAME).out  
    load                            
    b main                          
    b app_error_handler             
    monitor reset                   
    continue

1. breakpoints:

    b func
    b +offset
    b - offset
    b linenum
    b filename:linenum
    b filename:function
    b *address
    b
    b ... if cond
    tbreak args
    hbreak args
    thbreak args
    rbreak args
    info breakpoints [n]
    info break [n]
    info watchpoints [n]

    watch expr
    rwatch expr
    awatch expr

    catch event
    tcatch event

    clear
    clear function
    clear filename:function
    clear linenum
    clear filename:linenum

    delete [breakpoints] [range]

    disable [breakpoints] [range]
    enable [breakpoints] [range]
    enable [breakpoints] once range ...
    enable [breakpoints] delete range ...

    condition bnum expr
    condition bnum
    ignore bnum count

    commands bnum
    ... command-list
    end

2. continuing and stepping

    continue [ignore-count]
    c [ignore-count]
    fg [ignore-count]

    step
    step count
    next [count]

    finish
    until
    until location

    stepi
    si

    nexti
    ni

3. Stack frmames

    f args
    f n
    f addr
    up n
    down n

    info f

4. back traces

    breaktrace
    bt

    bt n
    bt -n
    
5. examing source files

    list linenum
    list function
    l
    l -
    set listsize [count]

6. examing data

    print expr
    print /f expr
    print *array@len

7. output format

    x -- hex
    d -- signed decimal
    u -- unsigned decimal
    o -- octal
    t -- t stands for two - binary
    a -- address
    c -- character
    f -- floating

