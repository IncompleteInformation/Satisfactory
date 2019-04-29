from . Material import Material

mats = [
    #Atomic
    "Power",
    "Limestone",
    "IronOre",
    "CopperOre",
    "Coal",
    "CrudeOil",
    "CateriumOre",

    #Normal
    "IronIngot",
    "IronPlate",
    "IronRod",
    "CopperIngot",
    "Wire",
    "Cable",
    "Biomass",
    "Concrete",
    "Screw",
    "ReinforcedIronPlate",
    "BioFuel",
    "Rotor",
    "ModularFrame",
    "PowerShard",
    "ColorCartridge"
    "Fabric",
    "SteelIngot",
    "SteelBeam",
    "SteelPipe",
    "EncasedIndustrialBeam",
    "Stator",
    "Motor",
    "HeavyModularFrame",
    "SpikedRebar",
    "CateriumIngot",
    "Quickwire",
    "Plastic",
    "Fuel",
    "Rubber",
    "CircuitBoard",
    "Computer",
    "Filter",
    "AILimiter",
    "Supercomputer",
    "HighSpeedConnector",

    #EquipmentWorkshop
    "PortableMiner",
    "XenoZapper",
    "ObjectScanner",
    "Beacon",
    "Chainsaw",
    "ColorGun",
    "Parachute",
    "RebarGun",
    "XenoBasher",
    "MedicinalInhaler",
    "BladeRunners",
    "GasMask",
    "JetPack",

    #MileStones -COMPLETELATER

    #PersonalBuild - Special
    "TheHUB",
    "SpaceElevator",

    #PersonalBuild - Production
    "CraftBench",
    "EquipmentWorkshop",

    "MinerMk1",
    "MinerMk2",

    "Smelter",
    "Foundry",

    "Constructor",
    "Assembler",
    "Manufacturer",

    "OilPump",
    "OilRefinery",

    #PersonalBuild - Power
    "BiomassBurner",
    "CoalGenerator",
    "FuelGenerator",
    "GeoThermalGenerator",

    "PowerPole",
    "PowerPoleMk2",
    "PowerPoleMk3",
    "PowerLine",
    #PersonalBuild - Logistics
    "ConveyorPole",
    "ConveyorPoleStackable",
    "ConveyorBelt",
    "ConveyorBeltMk2",
    "ConveyorBeltMk3",
    "ConveyorBeltMk4",

    "ConveyorSplitter",
    "SmartSplitter",
    "ProgrammableSplitter",
    "ConveyorMerger",

    #PersonalBuild - Foundations
    "Foundation8x4",
    "Foundation8x2",
    "Ramp8x4",
    "Ramp8x2",
    "StairsLeft",
    "StairsRight",

    #PersonalBuild - Walls
    "Wall", #all the same

    #PersonalBuild - Organization
    "PersonalStorageBox",
    "StorageContainer",
    "StorageContainerMk2",

    "JumpPad",
    "TiltedJumpPad",
    "UJellyLandingPad",

    "LookoutTower",

    "Walkway", #all the same

    #PersonalBuild - Vehicles
    "Tractor",
    "Truck",
    "TruckStation",
]

class Materials:
    def __init__(self):
        # self.X = Material("Power")
        for m in mats:
            exec(f'self.{m} = Material("{m}")')
    def __iter__(self):
        return iter(self.__dict__.values())
