### Binary Search
def binary_search(l, r):
    while l < r:
        m = l + (r - l) // 2
        if f(m):    # 判断找了没有，optional
            return m
        if g(m):
            r = m   # new range [l, m)
        else:
            l = m + 1 # new range [m+1, r)
    return l    # or not found


### BFS
  Q = []
  Q.append(S)
  visit = set([])
  level = 0
  while len(Q) > 0:
    cnt = len(Q)
    while cnt > 0:
      cnt -= 1
      top = Q[0]
      visit.add(top)
      del Q[0]
      for nei in neighbors[top]:
        if nei in visit:
          continue
        Q.append(nei)
    level += 1
### QuickSort
    def partition(self, nums, l, r) -> int:
        pi = random.randint(l, r)
        nums[l], nums[pi] = nums[pi], nums[l]
        p = nums[l]
        while l < r:
            while l < r and p <= nums[r]:
                r -= 1
            nums[l] = nums[r]
            while l < r and p >= nums[l]:
                l += 1
            nums[r] = nums[l]
        nums[l] = p
        return l

    def quickSort(self, nums, l, r) -> int:
        N = len(nums)
        if l < r:
            pi = self.partition(nums, l, r)
            self.quickSort(nums, l, pi - 1)
            self.quickSort(nums, pi + 1, r)
        return nums
### Inorder Traversal
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        st = []
        ans = []
        while len(st) > 0 or root != None:
            if root != None:
                st.append(root)
                root = root.left
            else:
                root = st[-1]
                st.pop()
                ans.append(root.val)
                root = root.right
        return ans
### ...
