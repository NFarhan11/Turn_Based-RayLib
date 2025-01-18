## Battle.py

### init

```
Start

DEFINE units_data = player_units + enemy_units
DEFINE battle_sprites = CALL SpriteGroup
DEFINE player_sprites = CALL SpriteGroup
DEFINE enemy_sprites = CALL SpriteGroup
DEFINE cmd_ui = CALL CommandUI

DEFINE current_unit = None
DEFINE turn_in_progress = False
DEFINE priority_queue = []

End
```

### setup

```
Start

CALL initialize_units FUNC
CALL initialize_priority_queue FUNC

End
```

### initialize_units

```
Start

FOR team, units in units_data
    FOR index, unit in {first 6 units each team}
        CALL create_unit FUNC

End
```

### create_unit

```
Start

DEFINE pos = (BATTLE_POSITIONS)[index]
DEFINE groups = [battle_sprites, player_sprites OR enemy_sprites]
CALL UnitSprite
CALL UnitNameSprite
CALL UnitStatsSprite

End
```

### initialize_priority_queue

```
Start

DEFINE combined_units = []
FOR unit_dict in units_data
    FOR unit in unit_dict
        APPEND combined_units

FOR index, unit in combined_units
    IF unit is_alive
        APPEND priority_queue = (-unit.SPD, index, unit)

HEAPQ HEAPIFY priority_queue

End
```

### process_turn

```
Start

IF turn_in_progress IS FALSE
    IF priority_queue IS EMPTY
        CALL repopulate_queue

IF priority_queue NOT EMPTY
    unit = HEAPQ HEAPPOP priority_queue
    IF unit is_alive
        current_unit = unit
        turn_in_progress IS TRUE
    ELSE
        CALL process_turn

End
```

### repopulate_queue

```
SAME AS initialize_priority_queue
```

### end_turn

```
Start

IF current_unit NOT EMPTY
    current_unit = None
    turn_in_progress IS FALSE
    CALL process_turn

End
```

### hightlight_unit

```
Start

FOR sprite IN battle_sprites
    IF sprite IS INSTANCEOF UnitSprite AND sprite.unit IS unit
    DEFINE sprite_pos = Vector2(sprite_pos)
    DRAW circle

End
```

### input

```
Start

IF KEY_F IS PRESSED
    CALL end_turn

End
```

### update

```
Start

CALL process_turn
CALL battle_sprites -> update()
CALL input

End
```

### draw

```
Start

CLEAR BACKGROUND
DRAW battle_sprites
DRAW cmd_ui

IF current_unit IS NOT EMPTY
    CALL hightlight_unit(current_unit)

End
```
