class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    stack = [self.root]
    while stack:
        current_node = stack.pop()
        if current_node.get('id') == id:
            return current_node
        stack.extend(current_node.get('children', []))
    return None
  
  def get_element_by_id_bfs(self, id):
    queue = [self.root]
    while queue:
        current_node = queue.pop(0)
        if current_node.get('id') == id:
            return current_node
        queue.extend(current_node.get('children', []))
    return None
     
        
