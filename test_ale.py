from random import randrange
from multi_agent_ale_py import ALEInterface
from dqn_files import *


ale = ALEInterface()
# Get & Set the desired settings
ale.setInt("random_seed", 123)
# Set USE_SDL to true to display the screen. ALE must be compilied
# with SDL enabled for this to work. On OSX, pygame init is used to
# proxy-call SDL_main.
USE_SDL = False
if USE_SDL:
    ale.setBool("sound", True)
    ale.setBool("display_screen", True)

# Load the ROM file
rom_file = "./Atari-2600-VCS-ROM-Collection/HC ROMS/BY ALPHABET/S-Z/Video Olympics - Pong Sports.bin"
ale.loadROM(str.encode(rom_file))

legal_actions = ale.getLegalActionSet()
print("Legal actions: {}".format(legal_actions))

modes = ale.getAvailableModes(num_players=2)
ale.setMode(modes[0])
ale.reset_game()

for episode in range(10):
    total_reward = 0
    while not ale.game_over():
        a = legal_actions[randrange(len(legal_actions))]
        # Apply an action and get the resulting reward
        reward = ale.act(a, a)
        total_reward += reward
    print("Episode %d ended with score: %d" % (episode, total_reward))
    ale.reset_game()
