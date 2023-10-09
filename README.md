# [CS:GO] Force Silenced

NOT MAINTAINED DUE TO CS2 REPLACING CSGO

Force Silenced is a CS:GO tool written in Python. It allows the user to completely disable `+attack2` while a silenced weapon is equipped.  
It does this by utilising CS:GO's Game State Integration to see which weapon is currently equipped. If it's one with a silencer, `mouse2` is unbound. Otherwise, it's rebound to `+attack2`.

## Performance
I didn't notice any real-world difference in input lag or FPS while playing matchmaking, but ran some rudimentary benchmarks on Ulletical's Benchmark Map.  
`Script on:`  Average framerate: 449.03  
`Script off:` Average framerate: 461.76  
This is a 2.6% decrease, but very much in the margin of error. Likely varies from system to system.  
Regardless, take the numbers with a pinch of salt as I was in a Discord call, with Spotify and Brave open at the same time. 

## Acknowledgements
 - [Erlendeikeland's Game State Integration Library](https://github.com/Erlendeikeland/csgo-gsi-python)

## Installation
- Drag `gamestate_integration_sarim.cfg` into your `Counter-Strike Global Offensive\csgo\cfg` folder.
- Add `-netconport 6313` to your launch options.
- Open `main.py` and turn on CS:GO.

## Support
- Open an issue on GitHub.
- DM me on Twitter, [@hk_sarim](https://twitter.com/hk_sarim).

