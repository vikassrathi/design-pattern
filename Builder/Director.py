


class Director:
    def __init__(self,builder):
        self.builder=builder


    def construct(self,cpu,gpu,storage,core,ram):
        self.builder.set_cpu(cpu)
        self.builder.set_gpu(gpu)
        self.builder.set_storage(storage)
        self.builder.set_ram(ram)
        self.builder.set_core(core)
        return  self.builder.build()
