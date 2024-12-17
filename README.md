# Pwnagotchi Clock/Calendar

![pic](https://i.imgur.com/iEbByAX.png)

## Installation

To install, first set your directory for custom plugins in your config file.  
Find or add `main.custom_plugins = "/custom/plugin/directory"` Initially, it may be empty.

After that, add `clock.py` to that folder.
Finally, enable it in your config.toml by adding the following line:

```toml
main.plugins.clock.enabled = true
main.plugins.clock.date_x_coord = 0
main.plugins.clock.date_y_coord = 96
main.plugins.clock.time_x_coord = 50
main.plugins.clock.time_y_coord = 96
main.plugins.clock.date_format = "%m/%d/%y"
main.plugins.clock.time_format = "%I:%M%p"
```

## FAQ

### The plugin doesn't work!

Bother me in my [discord server](https://discord.gg/VuhvYRz) (I am Logandev\_)
