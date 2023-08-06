from collections.abc import Iterable,Iterator
from typing import List

def chunking(sequence:Iterable,chunk_len:int)->Iterator:
    '''
    将输入序列切分成若干个块
    例如：sequence=[1,2,3,4,5,6,7,8,9,10],chunk_len=3
    返回：[[1,2,3],[4,5,6],[7,8,9],[10]]
    '''
    chunk,ct=[],0
    for item in sequence:
        chunk.append(item)
        ct+=1
        if ct%chunk_len==0:
            yield chunk
            chunk=[]
    if chunk:
        yield chunk


def lower_boundary(nums: List[object], target: object) -> object:
    '''
    在递增序列nums中查找target的下边界，即第一个大于等于target的数，并返回其下标
    例如：nums=[5,7,7,8,8,10],target=7
    返回：1

    '''
    l=0
    r=len(nums)
    while l<r:
        m=(l+r)//2
        if nums[m]<target:
            l=m+1  
        else:
            r=m
    return l

def upper_boundary(nums: List[object], target: object) -> object:
    '''
    在递增序列nums中查找target的上边界，即第一个大于target的数，并返回其下标
    例如：nums=[5,7,7,8,8,10],target=7
    返回：3

    '''
    l=0
    r=len(nums)
    while l<r:
        m=(l+r)//2
        if nums[m]<=target:
            l=m+1
        else:
            r=m
    return l
    



if __name__=='__main__':

    a=[5,7,7,8,8,10]
    print(lower_boundary(a,7))