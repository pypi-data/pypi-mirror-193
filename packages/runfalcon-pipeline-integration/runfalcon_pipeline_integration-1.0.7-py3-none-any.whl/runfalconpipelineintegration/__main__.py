import sys

from runfalconpipelineintegration.int_main_module import ModuleMain

def run():
    module_main:ModuleMain = ModuleMain()
    module_main.run(sys.argv[1:len(sys.argv)])

run()