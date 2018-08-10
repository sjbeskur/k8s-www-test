import CounterExample from 'components/counter-example'
import FetchData from 'components/fetch-data'
import HomePage from 'components/home-page'
import Hostname from 'components/hostname'
import Elements from 'components/elements'

export const routes = [
    { path: '/', component: HomePage, display: 'Home', style: 'glyphicon glyphicon-home' },
    { path: '/counter', component: CounterExample, display: 'Counter', style: 'glyphicon glyphicon-education' },
    { path: '/fetch-data', component: FetchData, display: 'Fetch data', style: 'glyphicon glyphicon-th-list' },
    { path: '/hostname', component: Hostname, display: 'Host info', style: 'glyphicon glyphicon-th-list' },
    { path: '/elements', component: Elements, display: 'Elements', style: 'glyphicon glyphicon-th-list' }
]