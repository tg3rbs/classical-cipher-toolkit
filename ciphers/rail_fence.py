def rail_fence_encrypt(text, rails):
    if rails <= 1:
        return text

    fence = [""] * rails
    rail = 0
    direction = 1

    for char in text:
        fence[rail] += char
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return "".join(fence)

def rail_fence_decrypt(text, rails):
    if rails <= 1:
        return text

    pattern = []
    rail = 0
    direction = 1

    for char in text:
        pattern.append(rail)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    result = [""] * len(text)
    index = 0

    for r in range(rails):
        for i in range(len(text)):
            if pattern[i] == r:
                result[i] = text[index]
                index += 1

    return "".join(result)