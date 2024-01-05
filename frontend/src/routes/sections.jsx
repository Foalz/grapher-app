import { lazy, Suspense } from "react";
import { Outlet, Navigate, useRoutes } from "react-router-dom";
import { NavigationBar } from "../layouts/navbar";

import Grapher from "../pages/grapher";
import About from "../pages/about";
import NotFound from "../pages/page404";

export default function Router() {
 const routes = useRoutes([
   {
     element: (
       <NavigationBar>
         <Outlet />
       </NavigationBar>
     ),
     children: [
       { element: <Grapher />, path: '/grapher' },
       { path: '/about', element: <About />, },
     ]
   },
   {
     path: '404',
     element: <NotFound />
   },
   {
     path: '*',
     element: <Navigate to="/404" replace />
   }
 ]);
 return routes;
}
