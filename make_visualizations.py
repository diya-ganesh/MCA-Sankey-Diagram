import pandas as pd
import sankey as sk
import plotly.graph_objects as go

def _code_mapping(df, src, targ):
    """ Map labels in src and targ columns to integers """
    df[src] = df[src].astype(str)
    df[targ] = df[targ].astype(str)

    # Get distinct labels
    list(set(list(df[src]) + list(df[targ])))
    labels = sorted(list(set(list(df[src]) + list(df[targ]))))

    # Get integer codes
    codes = list(range(len(labels)))

    # Create label to code mapping
    lc_map = dict(zip(labels, codes))

    # Substitute names for codes in dataframe
    df = df.replace({src: lc_map, targ: lc_map})
    return df, labels

def prepare_data(df, *cols, name='ArtistCount', count=20):
    """
    Prepare data for plotting
    :param df: Dataframe
    :param cols: all columns
    :param name: rename df column with index data
    :param count: minimum count required to be in plot
    """

    # 2. aggregate data grouping artists by columns
    agg_df = df.groupby(list(cols)).size().reset_index(name=name)
    #print(agg_df)

    # turn ints back to strings for sankey diagram
    for col in cols:
        if df[col].dtype == 'int64':
            agg_df = agg_df[agg_df[col] != 0]
            df[col] = df[col].astype('str')

    # 4. filter by certain count
    prepared_df = agg_df[agg_df[name] >= count]

    return prepared_df

def make_sankey(df, *cols, vals=None, **kwargs):
    """ Generate a sankey diagram
    df - Dataframe
    src - Source column
    targ - Target column
    vals - Values column (optional)
    optional params: pad, thickness, line_color, line_width """
    # create list
    stack_list = []

    # iterate through list of columns (minus 1 to prevent being out of index)
    # creating source and target for a column and the column after it and
    # appending it to the stack list
    for i in (range(len(cols) - 1)):
        curr_stack = df[[cols[i], cols[i + 1]]]
        curr_stack.columns = ['src', 'targ']
        stack_list.append(curr_stack)

    # concatenate the entire stack list as rows
    stacked = pd.concat(stack_list, axis=0)

    if vals:
        values = stacked[vals]
    else:
        values = [1] * len(stacked['src'])  # all 1

    stacked, labels = _code_mapping(stacked, 'src', 'targ')
    link = {'source': stacked['src'], 'target': stacked['targ'], 'value': values}

    pad = kwargs.get('pad', 50)
    thickness = kwargs.get('thickness', 50)
    line_color = kwargs.get('line_color', 'black')
    line_width = kwargs.get('line_width', 1)

    node = {'label': labels, 'pad': pad, 'thickness': thickness, 'line': {'color': line_color, 'width': line_width}}
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)

    width = kwargs.get('width', 800)
    height = kwargs.get('height', 400)
    fig.update_layout(
        autosize=False,
        width=width,
        height=height)
    return fig

def show_sankey(df, *cols, vals=None, **kwargs):
    fig = make_sankey(df, cols, vals, **kwargs)
    fig.show()

def main():
    # 1. convert data into pandas dataframe
    df = pd.read_json('/Users/Diya/Downloads/ds3500/hw2/artists.json')

    # ensure df only consists of nationality, gender and decade (int)
    artists_df = df[['Nationality', 'Gender']]
    artists_df['Decade'] = df['BeginDate'].astype('int64')
    artists_df['Decade'] = (artists_df['Decade'] // 10) * 10

    # 3. filter rows where decade is 0/missing data
    nonull_df = artists_df.dropna()
    nonull_df = nonull_df[nonull_df['Decade'] != 0]

    # 5.  Nationality (sources) & Decades (targets)
    nat_decade_df = prepare_data(nonull_df, 'Nationality', 'Decade', count=50)
    #print(nat_decade_df)
    nat_decade_sk = sk.make_sankey(nat_decade_df,'Nationality','Decade')
    nat_decade_sk.show()

    # 6. Nationality (sources) & Gender (targets)
    nat_gender_df = prepare_data(nonull_df, 'Nationality', 'Gender', count=50)
    #print(nat_gender_df)
    nat_gender_sk = sk.make_sankey(nat_gender_df,'Nationality','Gender')
    nat_gender_sk.show()

    # 7. Gender (sources) & Decade (targets)
    gender_decade_df = prepare_data(nonull_df, 'Gender', 'Decade', count=50)
    #print(gender_decade_df)
    gender_decade_sk = sk.make_sankey(gender_decade_df,'Gender','Decade')
    gender_decade_sk.show()

    # 8. 3 level sankey with Nationality, Gender, and Decade
    nat_gen_dec_df = prepare_data(nonull_df, 'Nationality', 'Gender', 'Decade', count=50)
    artists_sk = make_sankey(nat_gen_dec_df, 'Nationality', 'Gender', 'Decade')
    artists_sk.show()

if __name__ == '__main__':
    main()