EXEC	=	104neutrinos
SRC		=	104neutrinos.py

all:	$(EXEC)

$(EXEC):	$(SRC)
	@echo '#!/usr/bin/env python3' > $(EXEC)
	@cat $(SRC) >> $(EXEC)
	@chmod +x $(EXEC)

clean:
	@echo "Cleaning up..."

fclean: clean
	@rm -f $(EXEC)

re: fclean all

.PHONY: all clean re