
# coding:utf-8
import random
import bisect

# random.uniform(a,b)    用于生成一个指定范围内的随机浮点数，生成的随机整数a<=n<b.
# random.randint(a,b)    用于生成一个指定范围内的整数，a为下限，b为上限，生成的随机整数a<=n<=b;若a=b，则n=a；若a>b，报错
# random.shuffle(x[,random])    用于将一个列表中的元素打乱 （洗牌），会改变原始列表
# random.sample(sequence,k)    从指定序列中随机获取k个元素作为一个片段返回，不会改变原有序列
# random.choice(sequence)    从序列中获取一个随机元素，参数sequence表示一个有序类型，并不是一种特定类型，泛指list，tuple，字符串等
# 1. 把序列按权重值扩展成:lists=[A,A,A,A,A,B,B,C,C,D],然后random.choice(lists)随机选一个就行。虽然这样选取的时间复杂度是O(1)
# 2. 计算权重总和sum，然后在1到sum之间随机选择一个数R，之后遍历整个集合，统计遍历的项的权重之和，如果大于等于R，就停止遍历，选择遇到的项，它的时间复杂度是O（n）。
# 3. 可以先对原始序列按照权重排序。这样遍历的时候，概率高的项可以很快遇到，减少遍历的项。（因为rnd递减的速度最快(先减去最大的数)）
# 4. 先搞一个权重值的前缀和序列，然后在生成一个随机数t后，可以用二分法来从这个前缀和序列里找，那么选取的时间复杂度就是O(logn)了。

list = ['A', 'B', 'C', 'D']


def weight_choice(weight):
    """
    :param weight: list对应的权重序列
    :return:选取的值在原列表里的索引
    """
    weight_sum = []
    sum = 0
    for a in weight:
        sum += a
        weight_sum.append(sum)
    t = random.randint(0, sum - 1)
    return bisect.bisect_right(weight_sum, t)


if __name__ == "__main__":
    print(list[weight_choice([5, 2, 2, 1])])
