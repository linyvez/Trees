# Pre-order traversal
def pre_order(node):
    output = []
    current = node
    if current:
        output.append(current.data)
        if current.left:
            add = pre_order(current.left)
            output.append(*add) if isinstance(add[0], (int, str)) and len(add) == 1 else output.extend(add)
        if current.right:
            add = pre_order(current.right)
            output.extend(add) if isinstance(add[0], (int, str)) else output.extend(*add)
    return output

# In-order traversal
def in_order(node):
    output = []
    current = node
    if current:
        if current.left:
            add = in_order(current.left)
            output.append(*add) if isinstance(add[0], (int, str)) and len(add) == 1 else output.extend(add)
        output.append(current.data)
        if current.right:
            add = in_order(current.right)
            output.extend(add) if isinstance(add[0], (int, str)) else output.extend(*add)
    return output
        

# Post-order traversal
def post_order(node):
    output = []
    current = node
    if current:
        if current.left:
            add = post_order(current.left)
            output.append(*add) if isinstance(add[0], (int, str)) and len(add) == 1 else output.extend(add)
        if current.right:
            add = post_order(current.right)
            output.extend(add) if isinstance(add[0], (int, str)) else output.extend(*add)
        output.append(current.data)
    return output