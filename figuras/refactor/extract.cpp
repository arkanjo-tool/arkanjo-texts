void sort_and_print(vector<int> a){
	int n = a.size();
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n-1; j++){
			if(a[j] > a[j+1]){
				swap(a[j],a[j+1]);
			}
		}
	}
	for(int i = 0; i < n; i++){
		printf("%d ",&a[i]);
	}
}

vector<int> sort_increasing(vector<int> a){
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n-1; j++){
			if(a[j] > a[j+1]){
				swap(a[j],a[j+1]);
			}
		}
	}
	return a;
}

void print(vector<int> a){
	int n = a.size();
	for(int i = 0; i < n; i++){
		printf("%d ",&a[i]);
	}
}

void sort_and_print(vector<int> a){
	a = sort_inscreasing(a);
	print(a);
}


