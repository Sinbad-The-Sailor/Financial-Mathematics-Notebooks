problem forwardRatesLS;

param p;                 # Weight for price error
param dt;                # Discretization of forward rates
param n;                 # The number of forward rates
param m;                 # The number of continuously compounded spot rates

param M{1..m};           # The maturity for each continuously compounded spot rates
param r{1..m};	         # The continuously compounded spot rates

var f{0..n-1};           # Forward rates
var z{1..m};             # Price error

minimize obj: sum{j in 1..n-2} ((f[j+1] - 2*f[j] + f[j-1]))^2 + p * sum{i in 1..m} z[i]^2;

subject to pricing {i in 1..m}:
    sum{j in 0..M[i]/dt-1} f[j]*dt + z[i]*M[i] = r[i]*M[i];
