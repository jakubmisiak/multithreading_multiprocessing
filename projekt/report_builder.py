class ReportBuiler():

    def __init__(self):
        self.header_text = ''
        self.env_text = ''
        self.test_text= ''
        self.summary_text = '' 
        self.author_text = ''
        self.footer_text = ''

    def header(self):

        self.header_text = '''
        <html>
        <head>
        <title>Multithreading/Multiprocessing benchmark results</title>
        <style>

            body {
            font-size: 10pt;
            }

            h2 {
            padding-top: 10pt;
            }

            table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
            table-layout: fixed ;
            }

            td, th {
            border: 2px solid #b9b9b9;
            padding: 10px;
            text-align: center;
            width: 25% ;
            }

            th {
            background-color: #d5d5d5;
            }

            td {
            }

            tr:nth-child(odd) {
            background-color: #eeeeee;
            }
        </style>
        </head>
        <body>
        '''
        return self


    def env(self, **kwargs):

        self.env_text = '''
        <h1>Multithreading/Multiprocessing benchmark results</h1>
        <p>
        </p>
        <h2>Execution environment</h2>
        <p>

        Python version: {python_version}<br/>
        Interpreter: {interpreter}<br/>
        Interpreter version: {interpreter_version}<br/>
        Operating system: {os}<br/>
        Operating system version: {os_version}<br/>
        Processor: {cpu}<br/>
        CPUs: {cores}

        </p>

        <h2>Test results</h2>
        <p>The following table shows detailed test results:</p>
        <table>
        <tr>
            <th>Execution:</th>
            <th>1&nbsp;thread (s)</th>
            <th>4&nbsp;threads (s)</th>
            <th>4&nbsp;processes (s)</th>
            <th>processes based on number of CPUs (s)</th>
        </tr>
        '''.format(**kwargs)

        return self

    def test(self, *args):
        ex = [1,2,3,4,5]
        for a in range(0,5):
            self.test_text += f'<tr>\n'
            self.test_text += f'<td>{ex[a]}</td>\n'
            for i in range(0,4):
                print(i)
                self.test_text += f'<td>{"{:.3f}".format(args[0][i][a])}</td>\n'
            self.test_text += f'</tr>\n'
        return self

    def summary(self, *args):
        self.summary_text= ''' 
            </table>
            <h2>Summary</h2>
            <p>The following table shows the median of all results:</p>
            <table>
            <tr>
                <th>Execution:</th>
                <th>1&nbsp;thread (s)</th>
                <th>4&nbsp;threads (s)</th>
                <th>4&nbsp;processes (s)</th>
                <th>processes based on number of CPUs (s)</th>
            </tr>

            <tr>
                <td>Median:</td>'''
        for a in args[0]:
            self.summary_text += f'<td>{"{:.3f}".format(a)}</td>\n'

        self.summary_text+='''  </tr>

                                </table>'''
        return self
    
    def author(self, **kwargs):
        self.author_text = '<p>App author: {name}</p>\n'.format(**kwargs)
        return self

    def footer(self):
        self.footer_text = '''
        </body>
        </html>
        '''
        return self

    def build(self):
        return self.header_text + \
        self.env_text + \
        self.test_text + \
        self.summary_text + \
        self.author_text + \
        self.footer_text

