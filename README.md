# HMM_Calc
Functions for generating Alpha and Delta tables from a Hidden Markov Model. 

Parameters:

1. **a**: Matrix of transition probabilities. a[i][j] = a_{ij} = Probability of transitioning from state i to state j
2. **b**: Matrix of emission probabilities. b[i][x] = b_i(x) = Probability of emitting x at state i
3. **pi**: Array of start probabilities. pi[i] = pi_i = Probability of starting at state i
4. **sequence**: Array of integers corresponding to outputs. sequence[i] = The known output at time i

## Example:
    


      # Transition properties
      # a[i][j] = probability of traveling to state j from state i
      a = [[0.3, 0.3, 0.4],
           [0.2, 0.7, 0.1],
           [0.2, 0.5, 0.3]]

      # Emission probabilities
      # b[i][x] = Probability of emitting output x at state i
      b = [[0.1, 0.0, 0.9],
           [0.3, 0.4, 0.3],
           [0.7, 0.2, 0.1]]

      # pi[i] = Probability of starting at state i
      pi = [0.2, 0.5, 0.3]

      # Observed output sequence
      sequence = [1, 2, 3, 1, 1, 4]

      # Prints alpha table and returns matrix
      alpha_table = alpha(a, b, pi, sequence)

      # Prints delta table and returns matrix
      delta_table = delta(a, b, pi, sequence)
