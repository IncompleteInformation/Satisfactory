from . Recipe import Recipe

recipes = {
    "IronIngot1" : {
        "Inputs" : {
            "Power" : 4,
            "IronOre" : 30,
        },
        "Outputs" : {
            "IronIngot" : 30,
        },
        "Factory" : "Smelter",
    },
    "IronIngot2" : {
        "Inputs" : {
            "Power" : 16,
            "IronOre" : 15,
            "CopperOre" : 15,
        },
        "Outputs" : {
            "IronIngot" : 45,
        },
        "Factory" : "Foundry",
    },
    "CopperIngot1" : {
        "Inputs" : {
            "Power" : 4,
            "CopperOre" : 30,
        },
        "Outputs" : {
            "CopperIngot" : 30,
        },
        "Factory" : "Smelter",
    },
    "CateriumIngot1" : {
        "Inputs" : {
            "Power" : 4,
            "CateriumOre" : 60,
        },
        "Outputs" : {
            "CateriumIngot" : 15,
        },
        "Factory" : "Smelter",
    },
    "SteelIngot1" : {
        "Inputs" : {
            "Power" : 16,
            "IronOre" : 45,
            "Coal" : 45,
        },
        "Outputs" : {
            "SteelIngot" : 30,
        },
        "Factory" : "Foundry",
    },
    "SteelIngot2" : {
        "Inputs" : {
            "Power" : 16,
            "IronIngot" : 22.5,
            "Coal" : 45,
        },
        "Outputs" : {
            "SteelIngot" : 45,
        },
        "Factory" : "Foundry",
    },

    "IronPlate1" : {
        "Inputs" : {
            "Power" : 4,
            "IronIngot" : 30,
        },
        "Outputs" : {
            "IronPlate" : 15,
        },
        "Factory" : "Constructor",
    },
    "IronRod1" : {
        "Inputs" : {
            "Power" : 4,
            "IronIngot" : 15,
        },
        "Outputs" : {
            "IronRod" : 15,
        },
        "Factory" : "Constructor",
    },
    "Wire1" : {
        "Inputs" : {
            "Power" : 4,
            "CopperIngot" : 15,
        },
        "Outputs" : {
            "Wire" : 45,
        },
        "Factory" : "Constructor",
    },
    "Wire2" : {
        "Inputs" : {
            "Power" : 4,
            "CateriumIngot" : 7.5,
        },
        "Outputs" : {
            "Wire" : 67.5,
        },
        "Factory" : "Constructor",
    },
    "Wire3" : {
        "Inputs" : {
            "Power" : 4,
            "IronIngot" : 15,
        },
        "Outputs" : {
            "Wire" : 67.5,
        },
        "Factory" : "Constructor",
    },
    "Cable1" : {
        "Inputs" : {
            "Power" : 4,
            "Wire" : 30,
        },
        "Outputs" : {
            "Cable" : 15,
        },
        "Factory" : "Constructor",
    },
    "Cable2" : {
        "Inputs" : {
            "Power" : 15,
            "Wire" : 22.5,
            "Rubber" : 15,
        },
        "Outputs" : {
            "Cable" : 37.5,
        },
        "Factory" : "Assembler",
    },
    "Concrete1" : {
        "Inputs" : {
            "Power" : 4,
            "Limestone" : 45,
        },
        "Outputs" : {
            "Concrete" : 15,
        },
        "Factory" : "Constructor",
    },
    "Screw1" : {
        "Inputs" : {
            "Power" : 4,
            "IronRod" : 15,
        },
        "Outputs" : {
            "Screw" : 90,
        },
        "Factory" : "Constructor",
    },
    "Screw2" : {
        "Inputs" : {
            "Power" : 4,
            "IronIngot" : 15,
        },
        "Outputs" : {
            "Screw" : 90,
        },
        "Factory" : "Constructor",
    },
    "SteelBeam1" : {
        "Inputs" : {
            "Power" : 4,
            "SteelIngot" : 30,
        },
        "Outputs" : {
            "SteelBeam" : 10,
        },
        "Factory" : "Constructor",
    },
    "SteelPipe1" : {
        "Inputs" : {
            "Power" : 4,
            "SteelIngot" : 15,
        },
        "Outputs" : {
            "SteelPipe" : 15,
        },
        "Factory" : "Constructor",
    },
}

class Recipes:
    def __init__(self):
        for n,r in recipes.items():
            exec(f'self.{n} = Recipe("{n}",inputs={r["Inputs"]},outputs={r["Outputs"]},factory="{r["Factory"]}")')
    def __iter__(self):
        return iter(self.__dict__.values())
