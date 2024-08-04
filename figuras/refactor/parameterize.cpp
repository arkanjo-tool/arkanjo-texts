vector<int> sort_increasing(vector<int> a){
	int n = a.size();
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n-1; j++){
			if(a[j] > a[j+1]){
				swap(a[j],a[j+1]);
			}
		}
	}
	return a;
}

vector<int> sort_decreasing(vector<int> a){
	int n = a.size();
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n-1; j++){
			if(a[j] < a[j+1]){
				swap(a[j],a[j+1]);
			}
		}
	}
	return a;
}

vector<int> sort(
	vector<int> a, 
	function<bool(int,int)> cmp
){
	int n = a.size();
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n-1; j++){
			if(cmp(a[j],a[j+1]){
				swap(a[j],a[j+1]);
			}
		}
	}
	return a;
}
