function vector surface_bounce(const vector dir; const vector surf_nrm)
{
    /* Returns the vector of a vector bouncing of a surface normal. */
    vector bounce_dir = dir - surf_nrm * dot(dir, surf_nrm);
    return bounce_dir;
}

function int epsilon_compare(const float v1, v2, epsilon)
{
    /* Returns if the two values are close enough based on the epsilon */
    return v1 + epsilon > v2 && v1 - epsilon < v2;
}
