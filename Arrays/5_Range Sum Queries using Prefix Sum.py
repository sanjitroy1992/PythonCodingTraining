"""
Description : We are given an Array of n integers, We are given q queries having indices l and r . We have to find out sum between the given range of indices.
void fillPrefixSum(int arr[], int N, int prefixSum[])
    {
        prefixSum[0] = arr[0];

        // Adding present element
        // with previous element
        for (int i = 1; i < N; i++)
            prefixSum[i] = prefixSum[i-1] + arr[i];
    }

sumInRange = prefixSum[j]  , if i = 0

otherwise,

sumInRange = prefixSum[j] - prefixSum[i-1]  ,  if (i != 0).

"""


def calc_prefix_sum(arr):
    prefix_sum=[0]*(len(arr))
    print(prefix_sum)
    prefix_sum[0]=arr[0]
    for i in range(1,len(arr)):
        prefix_sum[i]=prefix_sum[i-1]+arr[i]
    return prefix_sum


arr=[0,1,2,3,4,5,6,7,8,9]
l=4
r=8
prefix_sum=calc_prefix_sum(arr)
if(l==0):
    ans=prefix_sum[r]
else:
    ans=prefix_sum[r] -prefix_sum[l-1]
print(prefix_sum)
print(ans)


