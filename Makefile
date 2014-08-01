mod:

	cd /Users/patrick/Library/Application\ Support/Steam/SteamApps/common/GarrysMod/garrysmod/addons; \
	git clone https://github.com/RafaelDeJongh/cap.git; \
	git clone https://github.com/RafaelDeJongh/cap_resources.git; \
	git clone https://github.com/wiremod/wire.git; \
	git clone https://github.com/RafaelDeJongh/cap_fonts; \
	git clone https://github.com/SnakeSVx/spacebuild.git; \

update:

	cd /Users/patrick/Library/Application\ Support/Steam/SteamApps/common/GarrysMod/garrysmod/addons; \
	cd cap; git pull; cd ..; \
	cd cap_resources; git pull; cd ..; \
	cd wire; git pull; cd ..; \
	cd cap_fonts; git pull; cd ..; \
	cd spacebuild; git pull; cd ..; \

