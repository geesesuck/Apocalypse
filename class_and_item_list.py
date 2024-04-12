import conditions

#Below are default classes
Mage ={"Health" : 15, "ArmorClass" : 14, "Skills":{"Burn":{"Damage":10,"Bonus": 2},"Zap":{"Damage":12,"Bonus": 1},"Chill":{"Damage":8,"Bonus": 3}}, "Stats":{"Dex":0,"Str":-1,"Wis":1,"Int":2}}
Thief ={"Health" : 17, "ArmorClass" : 15, "Skills":{"Stab":{"Damage":10,"Bonus": 3},"Slice":{"Damage":8,"Bonus": 4},"Poisoned Blade":{"Damage":12,"Bonus": 4, "Status": conditions.applyPoison}}, "Stats":{"Dex":2,"Str":0,"Wis":-1,"Int":1}}
Cleric = {"Health" : 20, "ArmorClass" : 16, "Skills":{"Hammer Slam":{"Damage":8,"Bonus": 3},"Smite":{"Damage":10,"Bonus": 2},"Cure Wounds":{"Healing": 8}}, "Stats":{"Dex":-1,"Str":1,"Wis":2,"Int":0}}
Warrior = {"Health" : 24, "ArmorClass" : 17, "Skills":{"Wrestle":{"Status": conditions.grappled,"Bonus": 2},"Shield Bash":{"Damage":12,"Bonus": 1},"Slash":{"Damage":10,"Bonus": 3}}, "Stats":{"Dex":1,"Str":2,"Wis":0,"Int":-1}}
Characters = {"mage": Mage,"cleric": Cleric,"warrior": Warrior,"thief": Thief}