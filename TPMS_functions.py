from numpy import sin, cos, tan


form = {
    "Schwarz P": lambda x, y, z: cos(x) + cos(y) + cos(z),
    "Double Primitive": lambda x, y, z: 0.5 * (cos(x) * cos(y) + cos(y) * cos(z) + cos(z) * cos(x)) + 0.2 * (cos(2 * x) + cos(2 * y) + cos(2 * z)),
    "Schwarz D": lambda x, y, z: sin(x) * sin(y) * sin(z) + sin(x) * cos(y) * cos(z) + cos(x) * sin(y) * cos(z) + cos(x) * cos(y) * sin(z),
    "Complementary D": lambda x, y, z: cos(3 * x + y) * cos(z) - sin(3 * x - y) * sin(z) + cos(x + 3 * y) * cos(z) + sin(x - 3 * y) * sin(z) + cos(x - y) * cos(3 * z) - sin(x + y) * sin(3 * z),
    "Double Diamond": lambda x, y, z: 0.5 * (sin(x) * sin(y) + sin(y) * sin(z) + sin(x) * sin(z)) + 0.5 * cos(x) * cos(y) * cos(z),
    "D'": lambda x, y, z: 0.5 * (cos(x) * cos(y) * cos(z) + cos(x) * sin(y) * sin(z) + sin(x) * cos(y) * sin(z) + sin(x) * sin(y) * cos(z)) - 0.5 * (sin(2 * x) * sin(2 * y) + sin(2 * y) * sin(2 * z) + sin(2 * z) * sin(2 * x)) - 0.2,
    "Gyroid": lambda x, y, z: cos(x) * sin(y) + cos(y) * sin(z) + cos(z) * sin(x),
    "G'": lambda x, y, z: sin(2 * x) * cos(y) * sin(z) + sin(2 * y) * cos(z) * sin(x) + sin(2 * z) * cos(x) * sin(y) + 0.32,
    "Double Gyroid": lambda x, y, z: 2.75 * (sin(2 * x) * sin(z) * cos(y) + sin(2 * y) * sin(x) * cos(z) + sin(2 * z) * sin(y) * cos(x)) - (cos(2 * x) * cos(2 * y) + cos(2 * y) * cos(2 * z) + cos(2 * z) * cos(2 * x)) - 0.95,
    "Karcher K": lambda x, y, z: 0.3 * (cos(x) + cos(y) + cos(z)) + 0.3 * (cos(x) * cos(y) + cos(y) * cos(z) + cos(z) * cos(x)) - 0.4 * (cos(2 * x) + cos(2 * y) + cos(2 * z)) + 0.2,
    "O, CT-O": lambda x, y, z: 0.6 * (cos(x) * cos(y) + cos(y) * cos(z) + cos(z) * cos(x)) - 0.4 * (cos(x) + cos(y) + cos(z)) + 0.25,
    "Lidinoid": lambda x, y, z: 0.5 * (sin(2 * x) * cos(y) * sin(z) + sin(2 * y) * cos(z) * sin(x) + sin(2 * z) * cos(x) * sin(y)) - 0.5 * (cos(2 * x) * cos(2 * y) + cos(2 * y) * cos(2 * z) + cos(2 * z) * cos(2 * x)) + 0.15,
    "Neovius": lambda x, y, z: 3 * (cos(x) + cos(y) + cos(z)) + 4 * cos(x) * cos(y) * cos(z),
    "I WP": lambda x, y, z: 2 * (cos(x) * cos(y) + cos(y) * cos(z) + cos(z) * cos(x)) - (cos(2 * x) + cos(2 * y) + cos(2 * z)),
    "Fisher-Koch S": lambda x, y, z: cos(2 * x) * sin(y) * cos(z) + cos(x) * cos(2 * y) * sin(z) + sin(x) * cos(y) * cos(2 * z),
    "Fisher-Koch C(S)": lambda x, y, z: cos(2 * x) + cos(2 * y) + cos(2 * z) + 2 * (sin(3 * x) * sin(2 * y) * cos(z) + cos(x) * sin(3 * y) * sin(2 * z) + sin(2 * x) * cos(y) * sin(3 * z)) + 2 * (sin(2 * x) * cos(3 * y) * sin(z) + sin(x) * sin(2 * y) * cos(3 * z) + cos(3 * x) * sin(y) * sin(2 * z)),
    "Fisher-Koch Y": lambda x, y, z: cos(x) * cos(y) * cos(z) + sin(x) * sin(y) * sin(z) + sin(2 * x) * sin(y) + sin(2 * y) * sin(z) + sin(x) * sin(2 * z) + sin(2 * x) * cos(z) + cos(x) * sin(2 * y) + cos(y) * sin(2 * z),
    "Fisher-Koch C(Y)": lambda x, y, z: -sin(x) * sin(y) * sin(z) + sin(2 * x) * sin(y) + sin(2 * y) * sin(z) + sin(x) * sin(2 * z) - cos(x) * cos(y) * cos(z) + sin(2 * x) * cos(z) + cos(x) * sin(2 * y) + cos(y) * sin(2 * z),
    "F-RD": lambda x, y, z: 4 * cos(x) * cos(y) * cos(z) - (cos(2 * x) * cos(2 * y) + cos(2 * x) * cos(2 * z) + cos(2 * y) * cos(2 * z))
}

