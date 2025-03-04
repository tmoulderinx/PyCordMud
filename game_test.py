"""
This module contains the game testing logic.
"""

import game
import gear
import consumables

def test_game_init_has_world():
    """
    Test case for initializing the game with a world.
    """
    # Arrange
    test_game = game.DiscordGame("Test Game")

    # Act
    test_game.create_map()

    # Assert
    assert test_game.get_map() is not None

def test_game_init_has_enemies():
    """
    Test case for initializing the game with enemies.
    """
    # Arrange
    test_game = game.DiscordGame("Test Game")

    # Act
    test_game.create_map()

    # Assert
    assert len(test_game.enemy_mgr.enemies) > 0

def test_game_add_player_increases_player_count():
    """
    Test case for adding a player to the game.
    """
    # Arrange
    test_game = game.DiscordGame("Test Game")
    tester_name = "Tester"

    # Act
    test_game.add_player(tester_name)

    # Assert
    assert test_game.is_playing(tester_name) is True

def test_game_move_player_has_moved():
    """
    Test case for moving the player.
    """
    # Arrange
    test_game = game.DiscordGame("Test Game")
    tester_name = "Tester"
    test_game.add_player(tester_name)

    # Act
    result = test_game.move_player(tester_name, "north")

    # Assert
    assert result is not None

def test_show_player_surroundings_has_contents():
    """
    Test case for showing the player surroundings with contents.
    """
    # Arrange
    test_game = game.DiscordGame("Test Game")
    tester_name = "Tester"
    test_player = game.PlayerCharacter(tester_name, test_game)
    test_game.add_player(test_player)

    # Act
    result = test_game.show_player_surroundings(tester_name)

    # Assert
    assert result is not None

#################################################
### Players, Enemies, Combat, And Consumables ###
#################################################

def test_player_gets_health_potion_on_duplicate_gear_acquisition():
    """
    Test if the player gets a health potion on duplicate gear acquisition.
    """
    # Arrange
    test_game = game.DiscordGame("Test Game")
    tester_name = "Tester"
    test_player = game.PlayerCharacter(tester_name, test_game)
    test_game.add_player(tester_name)
    test_gear = gear.Gear('Test Gear', 'A test piece of gear')
    cloned_test_gear = gear.Gear('Test Gear', 'A test piece of gear')
    test_health_potion = consumables.HealthPotion("Health Potion", "A potion that restores health.", 10)
    initial_consumables = len(test_player.consumables)

    # Act
    test_player.acquire_gear(test_gear)
    test_player.acquire_gear(cloned_test_gear)

    # Assert
    assert len(test_player.consumables) == initial_consumables + 1
    assert test_player.consumables[-1].name == test_health_potion.name

def test_game_player_use_potion_restores_health():
    """
    Test if the player's health is restored when using a health potion.
    """
    # Arrange
    test_game = game.DiscordGame("Test Game")
    tester_name = "Tester"
    test_player = game.PlayerCharacter(tester_name, test_game)
    test_game.add_player(tester_name)
    test_health_potion = consumables.HealthPotion("Health Potion", "A restorative potion.", 2)
    print(test_player.acquire_consumable(test_health_potion))

    # Act
    test_player.receive_damage(2)
    initial_health = test_player.health
    print(f'Test player consumables: {test_player.consumables}')
    print(test_game.use_consumable(tester_name, test_health_potion.name))

    # Assert
    assert test_player.health == initial_health + test_health_potion.health_points
