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

1. b -- set breakpoint
