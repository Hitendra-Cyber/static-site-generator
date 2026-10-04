def markdown_to_blocks(markdown: str) -> list[str]:
    final_list = []

    block_list = list(markdown.split('\n\n'))

    for block in block_list:
        if block == "":
            continue
        final_list.append(block.strip())

    return final_list