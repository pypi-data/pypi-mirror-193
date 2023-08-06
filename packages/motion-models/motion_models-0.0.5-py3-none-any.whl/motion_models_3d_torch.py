import torch
from pytorch3d.transforms import euler_angles_to_matrix


class MotionModel3DTorch:
    def __init__(self, selection, **kwargs):
        ''' Creates a 3D cone-beam motion model.

        :param selection: string selecting one of the types below
        :param kwargs: selection specific additional arguments like number of projections/ number of spline nodes
        '''
        if selection == 'rigid_3d':
            assert 'num_projections' in kwargs.keys(), 'Please provide the num_projections argument for the motion model.'
            self.free_parameters_per_node = 6
            self.free_parameters = self.free_parameters_per_node * kwargs['num_projections']
            self.eval = self.rigid_3d

    def rigid_3d(self, free_params, projection_matrices_input):
        '''Computes out = P @ M for M being a 3d rigid transformation matrix

        :param free_params: params for M; (rx, ry, rz, tx, ty, tz) for each projection as 1D torch tensor of size
        6*num_projections
        :param projection_matrices_input: the best guess for good projection matrices as 3D torch tensor of size
        3x4xnum_projections
        :return: the motion adjusted projection matrices as 3D torch tensor of size 3x4xnum_projections
        '''
        num_projections = projection_matrices_input.shape[2]
        assert (free_params.shape[0] == self.free_parameters), 'Wrong input to motion model rigid_3d.'

        euler_angles = torch.zeros((num_projections, 3), device=free_params.get_device())
        euler_angles[:, 0] = free_params[0::6]
        euler_angles[:, 1] = free_params[1::6]
        euler_angles[:, 2] = free_params[2::6]

        rotations = euler_angles_to_matrix(euler_angles, 'XYZ')
        rotations = torch.moveaxis(rotations, 0, 2)

        translations = torch.zeros((3, 1, num_projections), device=free_params.get_device())
        translations[0, 0, :] = free_params[3::6]
        translations[1, 0, :] = free_params[4::6]
        translations[2, 0, :] = free_params[5::6]

        lower_row = torch.zeros((1, 4, num_projections), device=free_params.get_device())
        lower_row[:, 3, :] = 1

        rigid_transform = torch.cat((torch.cat((rotations, translations), 1), lower_row), 0)
        # apply matrix multiplication along third dimension
        out = torch.einsum('ijn,jkn->ikn', projection_matrices_input, rigid_transform)

        return out


if __name__ == '__main__':
    m = MotionModel3DTorch('rigid_3d', num_projections=360)
    proj_mats_updated = m.eval(torch.rand(360 * 6).to('cuda'), torch.rand(3, 4, 360).to('cuda'))
    print('bla')