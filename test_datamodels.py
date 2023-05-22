from data.concrete import *


if __name__ == "__main__":

    mc = DataCache()
    dmns = DataCache()

    interfaces = ['Inlet1', 'Inlet2', 'outlet1', 'outlet2']

    dmn1 = Domain('Dmn1', interfaces)
    dmn2 = Domain('Dmn2', interfaces)
    dmns.add(dmn1)
    dmns.add(dmn2)

    gc1 = GasCompressor(
        'Axia Stage 1', 'Axial Compressor',
        'Inlet1', 'Outlet1', 'Blade1', 32, 'Z',
        59000, 'Axial Stage 1'        
    )

    gc2 = GasCompressor(
        'Centrifugal Stage 1', 'Centrifugal Compressor',
        'Inlet2', 'Outlet2', 'Blade2', 11, 'Z',
        59000, 'Centrifugal Stage 1'
    )

    pd1 = PipeDiffuser(
        'Pipe Diffuser', 'Pipe Diffuser', 'Throat1',
        'Inlet3', 'Outlet3', 21, 'Pipe Diffuser'
    )

    mc.add(gc1)
    mc.add(gc2)
    mc.add(pd1)
    print(mc)
    print(dmns)
