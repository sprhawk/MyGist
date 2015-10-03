Makefile
========

Wildcard directories
-------------------

    C_SOURCE_PATHS += $(sort $(dir $(wildcard $(SDK_PATH)**/**/)))
    INCLUDEPATHS += $(patsubst %, -I%, $(sort $(dir $(wildcard $(SDK_PATH)**/*.h))))
    
    C_SOURCE_PATHS += $(sort $(dir $(shell find $(SDK_PATH) -iname "*.c" -print)))
    INCLUDEPATHS += $(patsubst %, -I%, $(sort $(dir $(shell find $(SDK_PATH) -iname "*.h" -print))))

