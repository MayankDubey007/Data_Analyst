# List of names
actor_names = ['Ryan Reynolds', 'Benedict Cumberbatch', 'Robert Downey Jr.', 'Chris Evans']

# List of their ages
actor_ages = [48,62,54,np.nan ]

# Get the list of tuples by zipping the two lists together
list_of_tuples = list(zip(actor_names, actor_ages))

# Converting the list of tuples into pandas Dataframe
actor_df = pd.DataFrame(list_of_tuples, columns = ['Name', 'Age'])

# Print the dataframe
actor_df

