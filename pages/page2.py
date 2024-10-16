import streamlit as st

st.title("This is my first app")
st.write("hello")
if st.button('Click me!'):
    st.write('Button was clicked!')
 
st.markdown('**以下为打印的代码：**')
 
st.code('''
def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已经排好序，不需要再比较
        for j in range(0, n-i-1):
            # 如果元素比下一个元素大，则交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# 示例使用
if __name__ == "__main__":
    # 测试数据
    example_list = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", example_list)
    # 调用冒泡排序函数
    bubble_sort(example_list)
    print("排序后的数组:", example_list)
''', language='python')

 

