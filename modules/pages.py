from config import symbols, plots, dir

def create_pages():
    # First clear the markdown files before creating a new one
    for plot in plots:
        with open(f"{dir}mdwiki/content/trading-{plot}.md", "w") as external_file:
            external_file.close()

    # Then add the corresponding symbols to that file
    for plot in plots:
        # with open(f"{dir}mdwiki/content/{plot}.md", "a") as external_file:
        #     external_file.close()

        for symbol in symbols:
            with open(f"{dir}mdwiki/content/trading-{plot}.md", "a") as external_file:
                print(symbol)
                add_text = f"## {symbol}\n\n![](./plots/{plot}-{symbol}-1d.png)\n"
                print(add_text, file=external_file)
                external_file.close()
