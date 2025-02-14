Usual import
-------------

    import matplotlib.pyplot as plt
    %matplotlib inline
    %config InlineBackend.figure_format = 'svg'

    # Other usefull modules
    import matplotlib.ticker as ticker # tweak ticks
    import matplotlib.cm as cm         # tweak colormaps
    ...


Get current figure/axis
-----------------------

    fig = plt.gcf()
    ax = plt.gca()


Get the figure size
-------------------

    figsize = fig.get_size_inches()
    # or
    figsize = plt.gcf().get_size_inches()


Change major/minor ticks
------------------------

    import matplotlib.ticker as ticker

    # X-axis major/minor ticks (1 minor ticks between each major tick)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))

    # Y-axis major/minor ticks (1 minor ticks between each major tick)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(50))


