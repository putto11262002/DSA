package sort

import (
	"cmp"
)

// InsertionSort performs inplace Insertion Sort on the supplied slice. 
//
// Time Complexity: worse case O(n^2), average case O(n^2), best case O(n).
//
// Space Complexity: O(1).
//
// How Insertion Sort works: The algorithm divides the list into two sublists: 
// the partially sorted list (occupying the first part of the list) and 
// the unsorted list (occupying the remaining part of the list). Initially, 
// only the first element of the list is in the partially sorted sublist. 
// The algorithm grows the partially sorted list iteratively by taking the first element 
// of the unsorted sublist and inserting it into the correct position within the partially sorted sublist. 
// If the new element is less than the element to its left, swap the elements. 
// Continue swapping the new element leftwards until it is greater than or equal to 
// the element to its left, or until it reaches the beginning of the list.
func InsertionSort[V cmp.Ordered](a []V){
	for i := 1; i < len(a); i++{
		for j := i; j > 0 && a[j - 1] > a[j]; j-- {
			swap(j - 1, j, a)
		}
	}
}

func BubbleSort[V cmp.Ordered](a []V){

}

func SelectionSort[V cmp.Ordered](a []V){

}

func QuickSort[V cmp.Ordered](a []V){

}

func MergeSort[V cmp.Ordered](a []V){

}



// Swap performs an in place swap of the elements at index i and j in slice a.
// It expects i and j to be a valid index, it does not provide any checking for the supplied index.
func swap[V cmp.Ordered](i, j int, a []V){
	a[i], a[j] = a[j], a[i]
}

