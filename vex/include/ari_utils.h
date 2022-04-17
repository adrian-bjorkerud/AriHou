function vector surface_bounce(const vector dir; const vector surf_nrm)
{
    /* Returns the vector of a vector bouncing of a surface normal. */
    vector bounce_dir = dir - surf_nrm * dot(dir, surf_nrm);
    return bounce_dir;
}
